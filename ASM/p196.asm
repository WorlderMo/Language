assume cs:codesg

datasg segment
    dw 8 dup (0)
datasg ends

codesg segment
start:
    mov ax, datasg
    mov ss, ax
    mov sp, 16
    mov word ptr ss:[0], offset s
    mov ss:[2], cs
    call dword ptr ss:[0]
    nop
    s:
    mov ax, offset s
    sub ax, ss:[0cH]
    mov bx, cs
    sub bx, ss:[0eH]

    mov ax, 4c00h
    int 21h
codesg ends
end start
