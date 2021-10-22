import unittest
import binascii
from nessmith import assemble, NesSmithAssembleError


def x(s):
    return binascii.hexlify(s).decode('utf-8')


class TestNesSmith(unittest.TestCase):
    def test_assemble(self):
        bytes = assemble("")
        self.assertIsInstance(bytes, bytearray)
        bytes = assemble("", {})
        self.assertIsInstance(bytes, bytearray)

    def test_assemble_with_code(self):
        self.assertEqual(x(assemble("LDA $6001")), "ad0160")
        self.assertEqual(x(assemble("BRK")), "00")
        self.assertEqual(x(assemble("""
        LDA *$41
        JMP $1234

        ADC ($31,X)
        RTS
        """)), "a5414c3412613160")

        output = assemble("""
        LDA *$41
        label1:
        JMP $1234
        // melon farmer
        BEQ label1
        """)
        # print(map(lambda x: hex(x), output))
        self.assertEqual(x(output), "a5414c3412f0fb")

        self.assertEqual(x(assemble("""
LDA *$54
BNE BACK
LDA *$53
CMP #$30
BCS BACK

LDA *$50
ASL
RTS

BACK:
PLA
PLA
LDA #$01
STA $6000
JMP $874A
        """)), "a554d00aa553c930b004a5500a606868a9018d00604c4a87")

    def test_assemble_bad_opcode(self):
        with self.assertRaises(NesSmithAssembleError):
            assemble("LDA $123432")
        with self.assertRaises(NesSmithAssembleError):
            assemble("JHG\\HJ")


if __name__ == '__main__':
    unittest.main()
