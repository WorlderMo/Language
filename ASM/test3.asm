assume cs:code

stack segment
	db 128 dup (0)
stack ends

data segment
	db 20 dup (0)
code segment

start:
	mov ax,stack
	mov ss,ax
	mov sp,128

  ;-----安装程序并设置中断向量表----------------

	mov ax,0
	mov es,ax

	mov ax, data
	mov ds, ax
	push es:[9*4]
	pop ds:[0]
	push es:[9*4+2]
	pop ds:[2]

	mov word ptr es:[9*4],offset int9
	mov es:[9*4+2],cs


    mov ax, 0b800h
    mov es, ax
    mov bx,0
    mov cx,2000
s:  mov byte ptr es:[bx],' '
    add bx,2
    loop s

   call delay

   mov ah,4ch
   int 21h

delay:
	push ax
	push dx
	mov dx,0ffffh	;循环ffffffff次
	mov ax,0ffffh
s1:
	sub ax,1
	sbb dx,0
	cmp ax,0
	jne s1
	cmp dx,0
	jne s1
	pop dx
	pop ax
	ret

  ;-----以下为新的int 9 中断例程----------------

int9:
    push ax
	push bx
	push es

	in al,60h

	pushf
	pushf
	pop bx
	and bh,11111100b
	push bx
	popf
	call dword ptr ds:[0]

	cmp al,1fh
	jne int9ret


	mov al,2
	out 70h,al
	in al,71h

	mov ah,al
	mov cl,4
	shr ah,cl
	and al,00001111b


	add ah,30h
	add al,30h

	mov bx,0b800h
	mov es,bx
	mov byte ptr es:[160*8+20*2],ah
	mov byte ptr es:[160*8+20*2+1],71h
	mov byte ptr es:[160*8+20*2+2],al
	mov byte ptr es:[160*8+20*2+3],71h


int9ret:
	pop es
	pop bx
	pop ax
	iret
code ends
end start




