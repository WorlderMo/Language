assume cs:codesg

stack segment
    db 16 dup (0)
stack ends

codesg segment
start:
    mov ax, stack
    mov ss, ax
    mov sp, 16
    mov ax, 1000h
    push ax
    mov ax, 0
    push ax
    retf
codesg ends
end start
