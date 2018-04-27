assume cs: code, ds: data

data segment
	db 'welcome to masm!'
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov ax, 0B800h
	mov es, ax
	mov bx, 0
	mov si, 0
	mov di, 0

	mov cx, 16
s:
	mov bl, [si]
	mov bh, 00000010B
	mov word ptr es:[di+720h], bx    ;黑底绿色
	mov bh, 00100100B
	mov word ptr es:[di+720h+0A0H], bx    ;绿底红色
	mov bh, 01110001B
	mov word ptr es:[di+720h+0A0h+0A0h], bx    ;白底蓝色
	inc si
	add di, 2

	loop s

	mov ax, 4c00h
	int 21h

code ends
end start