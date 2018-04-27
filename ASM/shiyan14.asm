assume cs:code,ds:data
data segment
    db "YY/MM/DD HH:MM:SS"
    db 9,8,7,4,2,0
data ends
code segment
start:
    mov ax, data
    mov ds, ax
    mov cx, 6
    mov si, 0
    mov di, 17
s1:
    push cx
    mov al, [di]
    out 70h, al
    in al, 71h

    mov ah, al
    mov cl, 4
    shr ah, cl
    and al, 00001111b

    add al, 30h
    add ah, 30h
    mov [si], ah
    mov [si+1], al

    add si, 3
    add di, 1
    pop cx
    loop s1

    mov ax, data
    mov ds, ax
    mov si, 0
    mov cx, 17

    mov ax, 0b800h
    mov es, ax
    mov di, 160*13+32*2

s2:
    mov al, [si]
    mov es: [di],al
    mov al, 2
    mov es: [di+1],al

    inc si
    add di, 2
    loop s2

    mov ax, 4c00h
    int 21h

code ends
end start