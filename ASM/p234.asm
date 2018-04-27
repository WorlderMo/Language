assume cs: code

data segment
	db "Beginner's All-purpose Symbolic Instruction Code.", 0
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov si, 0
	call lettrc
	call show_str

	mov ax, 4c00h
	int 21h

lettrc:
	mov bl, [si]
	cmp bl, 0
	je lettrc_end
	cmp bl, 'a'
	jb lettrc_next
	cmp bl, 'z'
	ja lettrc_next
	and bl, 11011111b
	mov [si], bl

	lettrc_next:
	inc si
	jmp lettrc

	lettrc_end:
	ret

show_str:           ;显示字符串的子程序[定义开始]
	push ax   		;保存调用前寄存器环境
    push bx
    push cx
    push dx
    push es
    push si

    mov al, 0A0h     ;每行160个字节，即每行的长度为0A0h
    ;dec dh          ;行号在显存中下标从0开始,所以减1
    mul dh           ;行数和行长相乘得偏移地址
    mov bx, ax		 ;此时bx中存放的是第dh行的偏移地址
    mov al, 2        ;每个字符占两个字节，分别存放字符本身和其属性
    mul dl           ;得到列的偏移地址
    ;sub ax, 2       ;列号在显存中下标从0开始,又因为偶字节存放字符,所以减2
    add bx, ax       ;此时bx中存放的是行与列号的偏移地址
    mov ax, 0B800h   ;显存缓冲地址
    mov es, ax       ;ds中存放的是显存的第0页的起始的段地址
    mov di, 0
    mov al, 2
    mov ch, 0
    mov si, 0

show_str_s:
	mov cl, ds:[si]
    jcxz show_str_ok         ;判断cx是否为0，是否已经到达字符串的最后
    mov es:[bx+di], cl       ;偶地址存放字符
    mov es:[bx+di+1], al     ;奇地址存放字符的颜色属性
    inc si
    add di, 2                ;每个字符占两个字节，分别存放字符本身和其属性
    jmp short show_str_s     ;跳转到s标号处，继续判断cx是否为0

show_str_ok:
	pop si  				 ;恢复调用前寄存器环境
    pop es
    pop dx
    pop cx
    pop bx
    pop ax
    ret            		 ;显示字符串的子程序[定义结束]


code ends
end start

