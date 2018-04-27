assume cs: code, ds: data

data segment
	db 10 dup (0)
data ends

code segment
start:
    mov ax, 12666
    mov bx, data
    mov ds, bx
    mov si, 0
    call dtoc
    mov dh, 8
    mov dl, 3
    mov cl, 2
    call show_str

    mov ax, 4c00h
    int 21h
dtoc:                    ;数值显示的子程序定义
    push dx
    push cx
    push ax
    push si
    push bx
    mov bx, 0
s1:
	mov cx, 10
    mov dx, 0
    div cx
    mov cx, ax
    jcxz s2
    add dx, 30h
    push dx
    inc bx
    jmp short s1

s2:
	add dx, 30h
    push dx
    inc bx                   ;再进行一次栈操作(补充当"商为零而余数不为零"时的情况)
    mov cx, bx
    mov si, 0
s3:
	pop ax
    mov [si], al
    inc si
    loop s3

okay:
	pop bx
    pop si
    pop ax
    pop cx
    pop dx
    ret                      ;数值显示的子程序定义结束

show_str:
    push bx
    push cx
    push si
    mov al, 0A0h
    dec dh
    mul dh
    mov bx, ax
    mov al, 2
    mul dl
    sub ax, 2
    add bx, ax
    mov ax, 0B800h
    mov es, ax
    mov di, 0
    mov al, cl
    mov ch, 0
s:
	mov cl, ds:[si]
    jcxz ok
    mov es:[bx+di], cl
    mov es:[bx+di+1], al
    inc si
    add di, 2
    jmp short s

ok:
	pop si
    pop cx
    pop bx
    ret

code ends
end start
