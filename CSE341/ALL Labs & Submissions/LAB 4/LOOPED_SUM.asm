.MODEL SMALL
 
.STACK 100H

.DATA

; declare variables here

.CODE
MAIN PROC

; initialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here

MOV CX, 1
MOV DX, 1

L1:
CMP CX, 148
JE exit
ADD CX, 3
ADD DX, CX

JMP L1
exit:

;exit to DOS
               

MAIN ENDP
    END MAIN
