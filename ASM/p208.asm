assume cs: code,ss: stack

stack segment
    dw 8 dup(0)
stack ends

code segment
start:
    mov ax, stack
    mov ss, ax
    mov sp, 10h          ;设置栈段
    mov ax, 4240h        ;存储低位数据
    mov dx, 0fh          ;存储高位数据
    mov cx, 0ah          ;存储除数
    call divdw

    mov ax, 4c00h
    int 21h
divdw:                   ;子程序定义开始
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
                         ;子程序定义结束
code ends
end start