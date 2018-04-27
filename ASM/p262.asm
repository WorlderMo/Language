assume cs:code

data segment
	db 'welcome to masm!', 0
data ends

code segment
start:
	mov ax, cs
	mov ds, ax
	mov si, offset show
	mov ax, 0
	mov es, ax
	mov di, 200h
	mov cx, offset show_end - offset show
	cld
	rep movsb

	mov word ptr es:[7ch*4], 200h
	mov word ptr es:[7ch*4+2], 0

	mov dh, 10
	mov dl, 10
	mov cl, 2
	mov ax, data
	mov ds, ax
	mov si, 0
	int 7ch

	mov ax, 4c00h
	int 21h


show:
	mov ax, 0b800h
	mov es, ax
	mov al, 160
	mul dh
	mov di, ax
	mov al, 2
	mul dl
	add di, ax

show_s:
	cmp byte ptr [si], 0
	je show_ok
	mov al, [si]
	mov es:[di], al
	mov es:[di+1], cl
	inc si
	add di, 2
	jmp short show_s

show_ok:
	iret

show_end:
	nop

code ends
end start