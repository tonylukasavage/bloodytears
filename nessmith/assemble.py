from nessmith.ops import op_codes
import re

arg_formats = {
    'none': re.compile(r'^$'),
    'accumulator': re.compile(r'^A$'),
    'immediate': re.compile(r'^#\$(\d{2})$'),
    'zeropage': re.compile(r'^\$(\d{2})$'),
    'zeropagex': re.compile(r'^\$(\d{2}),x$'),
    'zeropagey': re.compile(r'^\$(\d{2}),y$'),
    'absolute': re.compile(r'^\$(\d{2})(\d{2})$'),
    'absolutex': re.compile(r'^\$(\d{2})(\d{2}),x$'),
    'absolutey': re.compile(r'^\$(\d{2})(\d{2}),y$'),
    'indirect': re.compile(r'^\(\$(\d{2})(\d{2})\)$'),
    'indirectx': re.compile(r'^\(\$(\d{2}),x\)$'),
    'indirecty': re.compile(r'^\(\$(\d{2})\),y$')
}

label_format = re.compile(r'^\w+$')

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
    output = bytearray()

    # line separate, trim, and filter out empty lines
    lines = map(lambda l: l.strip(), code.splitlines())

    # process each line of code
    line_count = 1
    for line in lines:
        # skip empty lines
        if __unwhite(line) == '':
            line_count += 1
            continue

        # separate op and its args, convert to lowercase, remove all whitespace
        tokens = list(map(lambda p: __unwhite(p.lower()), re.split(r'\s+', line, 2)))
        op, args = (tokens[0], tokens[1]) if len(tokens) > 1 else (tokens[0], '')

        # check if op is valid
        if op not in op_codes.keys():
            if args == '':
                if not label_format.search(op):
                    raise NesSmithAssembleError('Invalid label "' + op + '" on line ' + str(line_count), line_count, line)
                labels[op] = byte_count
                continue
            else:
                raise NesSmithAssembleError('Invalid op code "' + op + '" on line ' + str(line_count), line_count, code)

        # find what arg format is being used
        found = None
        for key in arg_formats:
            match = arg_formats[key].match(args)
            if match:
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
                raise

        except Exception:
            raise NesSmithAssembleError('Invalid args "' + op + '" on line ' + str(line_count), line_count, code)
        finally:
            line_count += 1

    return output

# read the sample code
# code = ''
# with open('test/code.asm', 'rb') as file:
#     code = file.read()
#     file.close()

# # convert sample code to byte code
# bytes = assemble(code, [])
# print(map(lambda x: hex(x), bytes))
#print(binascii.hexlify(bytes))
