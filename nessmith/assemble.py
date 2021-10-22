import binascii
from nessmith.ops import op_codes
import re

arg_formats = {
    'none': re.compile(r'^$'),
    'accumulator': re.compile(r'^A$'),
    'immediate': re.compile(r'^#\$([a-fA-F0-9]{2})$'),
    'zeropage': re.compile(r'^\*\$([a-fA-F0-9]{2})$'),
    'zeropagex': re.compile(r'^\*\$([a-fA-F0-9]{2}),x$'),
    'zeropagey': re.compile(r'^\*\$([a-fA-F0-9]{2}),y$'),
    'absolute': re.compile(r'^\$([a-fA-F0-9]{2})([a-fA-F0-9]{2})$'),
    'absolutex': re.compile(r'^\$([a-fA-F0-9]{2})([a-fA-F0-9]{2}),x$'),
    'absolutey': re.compile(r'^\$([a-fA-F0-9]{2})([a-fA-F0-9]{2}),y$'),
    'indirect': re.compile(r'^\(\$([a-fA-F0-9]{2})([a-fA-F0-9]{2})\)$'),
    'indirectx': re.compile(r'^\(\$([a-fA-F0-9]{2}),x\)$'),
    'indirecty': re.compile(r'^\(\$([a-fA-F0-9]{2})\),y$')
}

branch_ops = ['beq', 'bpl', 'bmi', 'bvc', 'bvs', 'bcc', 'bcs', 'bne']


class NesSmithAssembleError(Exception):
    def __init__(self, msg, line, code):
        self.msg = msg
        self.line = line
        self.code = code
        super().__init__(msg)


def __unwhite(str):
    return re.sub(r'\s+', '', str)


def assemble(code, vars={}):
    labels = {}
    byte_count = 0
    output = list()

    # line separate, trim, and filter out empty lines
    lines = map(lambda l: l.strip(), code.splitlines())

    # process each line of code
    line_count = 1
    for line in lines:
        # remove comments
        line = line.split('//')[0]

        # skip empty lines
        if __unwhite(line) == '':
            line_count += 1
            continue

        # check for label
        match = re.compile(r'^(\w+):$').match(line)
        if match:
            labels[match.group(1).lower()] = byte_count
            line_count += 1
            continue

        # separate op and its args, convert to lowercase, remove all whitespace
        tokens = list(map(lambda p: __unwhite(
            p.lower()), re.split(r'\s+', line, 2)))
        op, args = (tokens[0], tokens[1]) if len(
            tokens) > 1 else (tokens[0], '')

        # check if op is valid
        if op not in op_codes.keys():
            raise NesSmithAssembleError(
                'Invalid op code "' + op + '" on line ' + str(line_count), line_count, code)

        found = False
        # handle branch ops (first pass)
        if op in branch_ops:
            # TODO: validate label format
            output.extend([op_codes[op]['label'], args])
            byte_count += 2
            found = True
        # handle all other ops
        else:
            # find what arg format is being used
            for key in arg_formats:
                match = arg_formats[key].match(args)
                if match:
                    if key == 'none':
                        output.append(op_codes[op][key])
                        byte_count += 1
                    else:
                        # get little endian address
                        addr = list(match.groups())
                        addr.reverse()
                        addr = map(lambda a: int("0x" + a, 16), addr)
                        addr = list(addr)

                        # make list of byte code
                        output.extend([op_codes[op][key]] + addr)
                        byte_count += 1 + len(addr)

                    found = True
                    break

        try:
            if not found:
                raise Exception

        except Exception:
            raise NesSmithAssembleError(
                'Invalid args "' + op + '" on line ' + str(line_count), line_count, code)
        finally:
            line_count += 1

    # replace labels with distances in signed shorts
    for index, value in enumerate(output):
        if isinstance(value, str):
            labelPos = labels[value]
            # convert branch distance to signed short
            output[index] = ((labelPos - (index + 1)) +
                             (1 << 8)) % (1 << 8)

    return bytearray(output)

# read the sample code
# code = ''
# with open('test/code.asm', 'rb') as file:
#     code = file.read()
#     file.close()

# # convert sample code to byte code
# bytes = assemble(code, [])
# print(map(lambda x: hex(x), bytes))
# print(binascii.hexlify(bytes))
