; Nova OS Bootloader (16-bit Real Mode)
[BITS 16]
[ORG 0x7C00]
start:
    mov si, nova_msg
print_string:
    lodsb
    or al, al
    jz halt
    mov ah, 0x0E
    int 0x10
    jmp print_string
halt:
    cli
    hlt
nova_msg db 'Nova OS Kernel Loading...', 0
times 510-($-$$) db 0
dw 0xAA55
