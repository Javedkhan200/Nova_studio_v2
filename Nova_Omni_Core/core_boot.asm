; Nova Engine Low-Level Hardware Interface Stub
[BITS 32]
global _nova_hardware_init

section .text
_nova_hardware_init:
    xor eax, eax        ; Clear EAX Register (Status: OK)
    mov ebx, 0x1000     ; Set Base Memory Allocation Pointer
    mov ecx, 0x55AA     ; Boot Signature Validation Check
    ret                 ; Return control back to Nova C++ Core
