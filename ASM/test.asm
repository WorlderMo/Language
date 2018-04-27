assume cs:code

data segment
	db 224 dup('? ')
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov dl, 10h
	mov si, 0
	mov bh, 2
	mov cx, 224
ascii:
	mov byte ptr ds:[si], dl
	add si, 2
	inc dl
	loop ascii

show_ascii:
	push ax
	push bx
	push si
	push cx

	mov ax, 0B800h
	mov es, ax
	mov di, 0
	mov si, 0
	mov ah, 2
	mov bx, 0
	mov cx, 7
show:
	push cx
	mov cx,32
show_kid:

	mov al, ds:[si]
	mov es:[bx+di], al
	mov es:[bx+di+1], ah
	add si, 1
	add di, 2
	loop show_kid
	                ;mov di, 0
	pop cx
	add bx, 60h     ;add bx, 0a0h
	loop show

	pop cx
	pop si
	pop bx
	pop ax

	mov ax, 4c00h
	int 21h

code ends
end start