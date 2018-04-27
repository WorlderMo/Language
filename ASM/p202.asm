assume cs:codesg

datasg segment
    db 'conversation'
datasg ends

codesg segment
start:
    mov ax, datasg
    mov ds, ax
    mov si, 0
    mov cx, 12
    call capital

    mov ax, 4c00h
    int 21h

capital:
    and byte ptr [si], 11011111b
    inc si
    loop capital
    ret
codesg ends
end start
