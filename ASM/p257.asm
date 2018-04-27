assume cs:code

data segment
	db 'conversation', 0
data ends

code segment
start:
	mov ax, cs
	mov ds, ax
	mov si, offset nrptr
	mov ax, 0
	mov es, ax
	mov di, 200h
	mov cx, offset nrptrend - offset nrptr
	cld
	rep movsb

	mov word ptr es:[7ch*4], 200h
	mov word ptr es:[7ch*4+2], 0

	mov ax, data
	mov ds, ax
	mov si, 0
	mov ax, 0b800h
	mov es, ax
	mov di, 12*160+60

	mov bx, offset s - offset ok	;设置从标号ok到标号s的转移位移

s:
	cmp byte ptr [si], 0
	je ok				;如果是0跳出循环
	mov al, [si]
	mov es:[di], al
	mov ah, 2
	mov es:[di+1], ah
	inc si
	add di, 2
	int 7ch		;转移到标号s处

ok:
	mov ax, 4c00h
	int 21h

nrptr:
	push bp
	mov bp, sp
	add [bp+2], bx

nrptrret:
	pop bp
	iret

nrptrend:
	nop

code ends
end start