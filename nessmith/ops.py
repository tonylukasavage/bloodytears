op_codes = {
    'adc': {
        'immediate': 0x69,
        'zeropage': 0x65,
        'zeropagex': 0x75,
        'absolute': 0x6D,
        'absolutex': 0x7D,
        'absolutey': 0x79,
        'indirectx': 0x61,
        'indirecty': 0x71
    },
    'and': {
        'immediate': 0x29,
        'zeropage': 0x25,
        'zeropagex': 0x35,
        'absolute': 0x2D,
        'absolutex': 0x3D,
        'absolutey': 0x39,
        'indirectx': 0x21,
        'indirecty': 0x31
    },
    'asl': {
        'accumulator': 0x0A,
        'zeropage': 0x06,
        'zeropagex': 0x16,
        'absolute': 0x0E,
        'absolutex': 0x1E
    },
    'bit': {
        'zeropage': 0x24,
        'absolute': 0x2C
    },
    # 'bpl': {
    #     'branch': 0x24,
    # },
    # 'bmi': {
    #     'branch': 0x24,
    # },
    # 'bvc': {
    #     'branch': 0x24,
    # },
    # 'bvs': {
    #     'branch': 0x24,
    # },
    # 'bcc': {
    #     'branch': 0x24,
    # },
    # 'bcs': {
    #     'branch': 0x24,
    # },
    # 'bne': {
    #     'branch': 0x24,
    # },
    # 'beq': {
    #     'branch': 0x24,
    # },
    'brk': {
        'none': 0x00
    },
    'clc': {
        'none': 0x18
    },
    'cld': {
        'none': 0xD8
    },
    'cli': {
        'none': 0x58
    },
    'clv': {
        'none': 0xB8
    },
    'cmp': {
        'immediate': 0xC9,
        'zeropage': 0xC5,
        'zeropagex': 0xD5,
        'absolute': 0xCD,
        'absolutex': 0xDD,
        'absolutey': 0xD9,
        'indirectx': 0xC1,
        'indirecty': 0xD1
    },
    'cpx': {
        'immediate': 0xE0,
        'zeropage': 0xE4,
        'absolute': 0xEC
    },
    'cpy': {
        'immediate': 0xC0,
        'zeropage': 0xC4,
        'absolute': 0xCC
    },
    'dec': {
        'zeropage': 0xC6,
        'zeropagex': 0xD6,
        'absolute': 0xCE,
        'absolutex': 0xDE
    },
    'dex': {
        'none': 0xCA
    },
    'dey': {
        'none': 0x88
    },
    'eor': {
        'immediate': 0x49,
        'zeropage': 0x45,
        'zeropagex': 0x55,
        'absolute': 0x4D,
        'absolutex': 0x5D,
        'absolutey': 0x59,
        'indirectx': 0x41,
        'indirecty': 0x51
    },
    'inc': {
        'zeropage': 0xE6,
        'zeropagex': 0xF6,
        'absolute': 0xEE,
        'absolutex': 0xFE
    },
    'inx': {
        'none': 0xE8
    },
    'iny': {
        'none': 0xC8
    },
    'jmp': {
        'absolute': 0x4C,
        'indirect': 0x6C
    },
    'jsr': {
        'absolute': 0x20
    },
    'lda': {
        'immediate': 0xA9,
        'zeropage': 0xA5,
        'zeropagex': 0xB5,
        'absolute': 0xAD,
        'absolutex': 0xBD,
        'absolutey': 0xB9,
        'indirectx': 0xA1,
        'indirecty': 0xB1
    },
    'ldx': {
        'immediate': 0xA2,
        'zeropage': 0xA6,
        'zeropagey': 0xB6,
        'absolute': 0xAE,
        'absolutey': 0xBE
    },
    'ldy': {
        'immediate': 0xA0,
        'zeropage': 0xA4,
        'zeropagex': 0xB4,
        'absolute': 0xAC,
        'absolutex': 0xBC
    },
    'lsr': {
        'accumulator': 0x4A,
        'zeropage': 0x46,
        'zeropagex': 0x56,
        'absolute': 0x4E,
        'absolutex': 0x5E
    },
    'nop': {
        'none': 0xEA
    },
    'ora': {
        'immediate': 0x09,
        'zeropage': 0x05,
        'zeropagex': 0x15,
        'absolute': 0x0D,
        'absolutex': 0x1D,
        'absolutey': 0x19,
        'indirectx': 0x01,
        'indirecty': 0x11
    },
    'pha': {
        'none': 0x48
    },
    'php': {
        'none': 0x08
    },
    'pla': {
        'none': 0x68
    },
    'plp': {
        'none': 0x28
    },
    'rol': {
        'accumulator': 0x2A,
        'zeropage': 0x26,
        'zeropagex': 0x36,
        'absolute': 0x2E,
        'absolutex': 0x3E
    },
    'ror': {
        'accumulator': 0x6A,
        'zeropage': 0x66,
        'zeropagex': 0x76,
        'absolute': 0x6E,
        'absolutex': 0x7E
    },
    'rti': {
        'none': 0x40
    },
    'rts': {
        'none': 0x60
    },
    'sec': {
        'none': 0x38
    },
    'sed': {
        'none': 0xF8
    },
    'sei': {
        'none': 0x78
    },
    'sbc': {
        'immediate': 0xE9,
        'zeropage': 0xE5,
        'zeropagex': 0xF5,
        'absolute': 0xED,
        'absolutex': 0xFD,
        'absolutey': 0xF9,
        'indirectx': 0xE1,
        'indirecty': 0xF1
    },
    'sta': {
        'zeropage': 0x85,
        'zeropagex': 0x95,
        'absolute': 0x8D,
        'absolutex': 0x9D,
        'absolutey': 0x99,
        'indirectx': 0x81,
        'indirecty': 0x91
    },
    'stx': {
        'zeropage': 0x86,
        'zeropagey': 0x96,
        'absolute': 0x8E
    },
    'sty': {
        'zeropage': 0x84,
        'zeropagex': 0x94,
        'absolute': 0x8C
    },
    'tax': {
        'none': 0xAA
    },
    'tay': {
        'none': 0xA8
    },
    'tsx': {
        'none': 0xBA
    },
    'txa': {
        'none': 0x8A
    },
    'txs': {
        'none': 0x9A
    },
    'tya': {
        'none': 0x98
    },
}
