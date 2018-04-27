assume cs: code

data segment

    db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
    db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
    db '1993','1994','1995'    ;年份

    dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
    dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000    ;公司总收入

    dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
    dw 11542,14430,15257,17800     ;公司雇员人数

data ends

table segment
    db 21 dup('year summ ne ?? ')    ;table段的内容和容量
table ends

stack segment
	dw 64 dup(0)		;开辟栈段储存需要暂存的数据
stack ends

buffer segment
	db 64 dup(0)		;作为一个缓冲区，用于储存转化后的字符串，不至于混乱
buffer ends

code segment
start:
	mov ax, data
    mov ds, ax
    mov ax, table
    mov es, ax
    mov bx, 0
    mov si, 0
    mov di, 0
    call data_struct		;调用data_struct子程序结构化初始数据在table段

    mov ax, stack
    mov ss, ax
    mov sp, 128			;设置栈段

    mov ax, buffer
    mov ds, ax
    mov si, 0 			;ds:[si]指向buffer段
    mov ax, table
    mov es, ax			;es:[bx]指向table段
    mov bx, 0
    mov dh, 3           ;设置要显示的第一行行号

    mov cx, 21          ;循环次数，有几行数据就循环几次

s:
	push cx				;把程序压栈，保存循环次数

	mov ax, es:[bx]		;把年份信息写入buffer中
	mov ds:[si], ax
	mov ax, es:[bx+2]
	mov ds:[si+2], ax
	mov byte ptr ds:[si+4], 0   ;以0为结束字符
	mov dl, 20 					;第几列
	mov cl, 2 					;颜色属性
	call show_str				;调用子程序show_str，显示字符串

	push dx						;保存行和列的信息（主要是行）
	mov ax, es:[bx+5]			;读取收入信息,(低位数据)
	mov dx, es:[bx+7]			;高位数据
	call dtoc_dw 				;调用dtoc_dw把数值转化成字符串并写入到buffer中
	pop dx
    mov dl, 30                  ;把收入信息显示在第几列
    call show_str

    push dx
	mov ax, es:[bx+0ah]         ;读取一条总人数信息
	mov dx, 0
	call dtoc_dw                ;调用dtoc_dw将数值转换成字符串并写入到buffer中
	pop dx
	mov dl, 40
	call show_str

 	push dx

    mov ax, es:[bx+0dh]       	;读取一条人均收入信息
    mov dx, 0
    call dtoc_dw         		;调用dtoc_dw将数值转换成字符串到buffer中
    pop dx
    mov dl,50
    call show_str

    add dh, 1         			;一行打印一条数据
    add bx, 10h     			;让es:bx指向table的下一行数据

    pop cx						;cx出栈，恢复循环次数
    loop s

    mov ax,4c00h
    int 21h


data_struct:				;结构化数据储存在table段[子程序定义开始]
	push ax
	push bx
	push di
	push si
	push cx

	mov cx, 21 				;循环次数，有几行数据就循环几次

data_struct_s:
    mov ax, [bx]
    mov es:[di], ax
    mov ax, [bx+2]
    mov es:[di+2], ax   		;以上数据表示年份写入到table段

    mov ax, 54h[bx]
    mov dx, 56h[bx]
    mov es:5h[di], ax
    mov es:7h[di], dx   		;以上4句的作用是存放公司总收入

    mov ax, 0A8h[si]
    mov es:0Ah[di], ax  		;以上两句的作用是存放公司的雇员数

    mov ax, 54h[bx]
    div word ptr 0A8h[si]
    mov es:0dh[di], ax  		;以上三句的作用是存放公司的人均收入

    add bx, 4
    add di, 16
    add si, 2           		;以上3句是为下一次循环时存放数据做准备
    loop data_struct_s

    pop cx
	pop si
    pop di
    pop bx
    pop ax
    ret				;[子程序定义结束]


divdw:                   ;[子程序定义开始]
    push ax              ;先把低位数据压入栈
    mov ax, dx           ;把高位数据传给存储被除数的ax
    mov dx, 0
    div cx               ;先进行高位的除法
    mov bx, ax           ;把商赋值给bx，把ax空出来，以进行下次的除法运算
    pop ax               ;从栈中获取低位数据
    div cx               ;进行低位的除法
    mov cx, dx           ;把余数赋值给cx
    mov dx, bx           ;把高位除法运算得到的商赋值给dx
    ret                  ;程序返回，继续运行，[子程序定义结束]

dtoc_dw:                 ;[子程序定义开始]
    push ax
    push bx
    push cx
    push si
    push es
    push bp

    mov bp, 0

dtoc_dw_s0:
    mov cx, 10d 		 ;除以10，得到十进制数码值
    call divdw			 ;防止除法溢出，调用divdw子程序
    push cx 			 ;把余数压栈
    inc bp				 ;记录余数个数
    mov cx, ax			 ;把商传给cx，判断是否为0
    inc cx 				 ;若商已为0，则cx+1是为了在loop中cx-1=0，从而顺利结束loop循环
    loop dtoc_dw_s0

    mov cx, bp			 ;循环次数

dtoc_dw_s1:
    pop bx 				 ;把余数依次出栈
    add bl, 30h			 ;得到数值的ASCII码
    mov ds:[si], bl 	 ;把数值的ASCII码写入到buffer中
    inc si
    loop dtoc_dw_s1

    mov byte ptr ds:[si], 0 	;以0为结束字符

    pop bp
    pop es
    pop si
    pop cx
    pop bx
    pop ax
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
    mov al, cl
    mov ch, 0

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