assume cs:code

code segment

s1: db 'Good,better,best,','$'
s2: db 'Never let it rest,','$'
s3: db 'Till good is better,','$'
s4: db 'And better,best.','$'
s: dw offset s1, offset s2, offset s3, offset s4
row:  db 2, 4, 6, 8

start:
    mov ax, cs
    mov ds, ax               ;将ds也指向了cs段
    mov bx, offset s         ;(bx)=s标号地址
    mov si, offset row       ;（si）=row标号的地址。
    mov cx, 4                ;计数器置为4,4行字符串
ok:    						 ;在DOS窗口设置光标的位置
    mov bh,0             	 ;BIOS中的10h中断例程的入口参数设置，bh（页号）=0
    mov dh, [si]             ;入口参数：dh（行号）=（si）
    mov dl, 20               ;入口参数：dl（列数）=0
    mov ah, 2                ;10h例程中的2号子程序，功能：设置光标位置。
    int 10h                  ;调用中断例程
   							 ;开始显示字符串。调用21h例程，9号子程序
    mov dx,[bx]              ;入口参数：dx=（bx），每个字符串的首地址。
    mov ah,9             	 ;dos系统中21h例程中的9号子程序
    int 21h                  ;调用中断例程，功能：显示字符串（以$结尾的）
    inc si                   ;si按字节定义的。每次增量是1个字节。
    add bx,2             	 ;bx是按照字定义的，每次增量是2个字节。
    loop ok

    mov ax,4c00h
    int 21h

code ends
end start