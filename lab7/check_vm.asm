bits 64
section .data
    vm: db "vm", 10
    not_vm: db "not vm", 10


section .text
    global _start


_start:
    rdtscp
    mov r10, rax

    cpuid

    rdtscp
    sub r10, rax
    neg r10

    mov rax, 1

    cmp r10, 4000
    jge is_vm

    mov rdi, 1
    mov rsi, not_vm
    mov rdx, 7
    jmp _exit

is_vm:
    mov rdi, 1
    mov rsi, vm
    mov rdx, 4

_exit:
    syscall
    mov eax, 60
    mov rdi, 0
    syscall
