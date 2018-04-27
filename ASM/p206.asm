assume cs: code

data segment
	db 'welcome to masm!', 0
data ends

code segment
start:
	mov dh, 8       ;行号
	mov dl, 3       ;列号
	mov cl, 2       ;颜色属性
	mov ax, data
	mov ds, ax
	mov si, 0
	call show_str   ;设置基本参数

	mov ax, 4c00h
	int 21h

show_str:            ;显示字符串的子程序[定义开始]
	push ax   ;保存调用前寄存器环境
    push bx
    push cx
    push dx
    push es
    push si

    mov al, 0A0h     ;每行160个字节，即每行的长度为0A0h
    dec dh           ;行号在显存中下标从0开始,所以减1
    mul dh           ;行数和行长相乘得偏移地址
    mov bx, ax		 ;此时bx中存放的是第dh行的偏移地址
    mov al, 2        ;每个字符占两个字节，分别存放字符本身和其属性
    mul dl           ;得到列的偏移地址
    sub ax, 2        ;列号在显存中下标从0开始,又因为偶字节存放字符,所以减2
    add bx, ax       ;此时bx中存放的是行与列号的偏移地址
    mov ax, 0B800h   ;显存缓冲地址
    mov es, ax       ;es中存放的是显存的第0页(共0--7页)的起始的段地址
    mov di, 0
    mov al, cl
    mov ch, 0

s:
	mov cl, ds:[si]
    jcxz ok                  ;判断cx是否为0，是否已经到达字符串的最后
    mov es:[bx+di], cl       ;偶地址存放字符
    mov es:[bx+di+1], al     ;奇地址存放字符的颜色属性
    inc si
    add di, 2                ;每个字符占两个字节，分别存放字符本身和其属性
    jmp short s              ;跳转到s标号处，继续判断cx是否为0

ok:
	pop si  ;恢复调用前寄存器环境
    pop es
    pop dx
    pop cx
    pop bx
    pop ax
    ret            ;显示字符串的子程序[定义结束]

code ends
end start
