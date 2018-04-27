assume cs:codesg

codesg segment
start:
    mov ax, 2000h
    mov ds, ax
    mov bx, 0
    s:
    mov cl, [bx]
    mov ch, 0
    inc cx
    inc bx
    loop s

    ok:
    dec bx    ;bx=bx-1
    mov dx, bx

    mov ax, 4c00h
    int 21h
codesg ends
end start
