assume cs: code

code segment
start:
	a dw 1, 2, 3, 4, 5, 6, 7, 8
	b dd 0

	mov si, 0
	mov cx, 0
s:
	mov ax, a[si]
	add word ptr b, ax
	adc word ptr b[2], 0
	add si, 2
	loop s

	mov ax, 4c00h
	int 21h

code ends
end start