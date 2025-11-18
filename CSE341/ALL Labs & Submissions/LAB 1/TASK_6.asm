.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here
A DB 2
B DB 10
C DB ?

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here    

INC B
MOV CH, A
ADD CH, B       

MOV C, CH 

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
	END MAIN
