assume cs: code, ds: data

data segment
    db 10 dup (0)
data ends

buffer segment
    db 32 dup(0)        ;作为一个缓冲区，用于储存转化后的字符串，不至于混乱
buffer ends

code segment
start:
    mov ax, 9768h
    mov dx, 5Ah         ;被除数
    mov cx, 100d        ;除数
    call divdw
    mov bx, data
    mov ds, bx
    mov bx, buffer
    mov es, bx
    mov si, 0
    call dtoc_dw
    mov dh, 8
    mov dl, 3
    mov cl, 2
    call show_str

    mov ax, 4c00h
    int 21h

divdw:                   ;除法溢出子程序定义开始
    push ax              ;先把低位数据压入栈
    mov ax, dx           ;把高位数据传给存储被除数的ax
    mov dx, 0
    div cx               ;先进行高位的除法
    mov bx, ax           ;把商赋值给bx，把ax空出来，以进行下次的除法运算
    pop ax               ;从栈中获取低位数据
    div cx               ;进行低位的除法
    mov cx, dx           ;把余数赋值给cx
    mov dx, bx           ;把高位除法运算得到的商赋值给dx
    ret                  ;程序返回，继续运行
                         ;除法溢出子程序定义结束

dtoc_dw:        ;数值显示的子程序定义
    push ax
    push bx
    push cx
    push si
    push es

    mov bp, 0

dtoc_dw_s0:
    mov cx, 10d
    call divdw
    push cx
    inc bp
    mov cx, ax
    inc cx
    loop dtoc_dw_s0

    mov cx, bp

dtoc_dw_s1:
    pop bx
    add bl, 30h
    mov es:[si], bl
    inc si
    loop dtoc_dw_s1

    mov byte ptr es:[si], 0

    pop es
    pop si
    pop cx
    pop bx
    pop ax
    ret         ;数值显示的子程序定义结束

show_str:       ;显示字符串子程序定义
    push bx             ;保存调用前寄存器环境
    push cx
    push si
    mov al, 0A0h        ;每行160个字节，即每行的长度为0A0h
    dec dh              ;行号在显存中下标从0开始,所以减1
    mul dh              ;行数和行长相乘得偏移地址
    mov bx, ax          ;此时bx中存放的是第dh行的偏移地址
    mov al, 2           ;每个字符占两个字节，分别存放字符本身和其属性
    mul dl              ;得到列的偏移地址
    sub ax, 2           ;列号在显存中下标从0开始,又因为偶字节存放字符,所以减2
    add bx, ax          ;此时bx中存放的是行与列号的偏移地址
    mov ax, 0B800h      ;显存缓冲地址
    mov ds, ax          ;ds中存放的是显存的第0页(共0--7页)的起始的段地址
    mov di, 0
    mov al, cl
    mov ch, 0
s:
    mov cl, es:[si]
    jcxz ok                     ;判断cx是否为0，是否已经到达字符串的最后
    mov ds:[bx+di], cl          ;偶地址存放字符
    mov ds:[bx+di+1], al        ;奇地址存放字符的颜色属性
    inc si
    add di, 2                   ;每个字符占两个字节，分别存放字符本身和其属性
    jmp short s                 ;跳转到s标号处，继续判断cx是否为0

ok:
    pop si                      ;恢复调用前寄存器环境
    pop cx
    pop bx
    ret             ;显示字符串子程序定义结束

code ends
end start