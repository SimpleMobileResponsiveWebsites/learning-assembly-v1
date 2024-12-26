import streamlit as st

# App Title
st.title("Learn Assembly Programming")

# Sidebar Navigation
menu = ["Introduction", "Setup Environment", "Core Instructions", "Practice Examples", "Resources"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Introduction":
    st.header("Introduction to Assembly Programming")
    st.markdown("""
    Assembly language is a low-level programming language that allows you to write instructions directly for the computer's processor. It is architecture-specific, meaning different processors (like x86, ARM) have their own assembly languages.

    ### Key Concepts
    - **Registers**: Small storage locations in the CPU (e.g., AX, BX for x86).
    - **Instructions**: Commands like `MOV`, `ADD`, and `SUB` that the CPU executes.
    - **Memory Access**: Directly manipulate memory addresses and pointers.
    - **Flags**: Indicators like zero, carry, and overflow used for conditions.

    Example Instruction:
    ```assembly
    MOV AX, 5  ; Move the value 5 into the AX register
    ADD AX, 2  ; Add 2 to AX
    ```
    """)

elif choice == "Setup Environment":
    st.header("Setting Up Your Environment")
    st.markdown("""
    ### Choose an Architecture
    - **x86**: Common for PCs.
    - **ARM**: Popular for mobile devices.

    ### Tools for Programming and Debugging
    - **Windows**: MASM, TASM for x86 assembly.
    - **Linux**: `nasm` or `as` (GNU Assembler).
    - **Online Simulators**: [EASY68k](http://www.easy68k.com/), [emu8086](https://emu8086.com/).

    ### Install Debuggers
    - **GDB**: For Linux.
    - **OllyDbg**: For Windows.

    """)

elif choice == "Core Instructions":
    st.header("Core Assembly Instructions")
    st.markdown("""
    ### Key Instructions to Learn

    - **Data Transfer**: `MOV`, `PUSH`, `POP`
    - **Arithmetic Operations**: `ADD`, `SUB`, `MUL`, `DIV`
    - **Logical Operations**: `AND`, `OR`, `XOR`, `NOT`
    - **Comparison and Jumps**: `CMP`, `JMP`, `JE`, `JNE`, `JG`, `JL`

    Example:
    ```assembly
    section .data
        num1 db 10
        num2 db 20
    section .text
    global _start
    _start:
        MOV AL, [num1]  ; Load num1 into AL register
        ADD AL, [num2]  ; Add num2 to AL
        ; Exit program (Linux)
        MOV EAX, 1
        INT 0x80
    ```
    """)

elif choice == "Practice Examples":
    st.header("Practice Assembly Programming")

    st.markdown("""
    ### Example 1: Hello, World! Program (x86 Linux)
    ```assembly
    section .data
        msg db "Hello, World!", 0xA
        len equ $ - msg
    section .text
    global _start
    _start:
        ; Write to stdout
        MOV EAX, 4      ; syscall: write
        MOV EBX, 1      ; file descriptor: stdout
        MOV ECX, msg    ; message address
        MOV EDX, len    ; message length
        INT 0x80        ; make syscall
        ; Exit
        MOV EAX, 1      ; syscall: exit
        XOR EBX, EBX    ; status: 0
        INT 0x80
    ```

    ### Example 2: Add Two Numbers
    ```assembly
    section .data
        num1 db 5
        num2 db 7
    section .text
    global _start
    _start:
        MOV AL, [num1]  ; Load num1
        ADD AL, [num2]  ; Add num2
        ; Exit program
        MOV EAX, 1
        INT 0x80
    ```
    """)

    st.markdown("Try writing and testing these examples in an assembly simulator or your setup.")

elif choice == "Resources":
    st.header("Further Resources for Learning")
    st.markdown("""
    - **Books**:
      - [Programming from the Ground Up](https://savannah.nongnu.org/projects/pgubook): A great beginner-friendly book for x86 assembly.
    - **Online Tools**:
      - [EASY68k](http://www.easy68k.com/): A simulator for assembly programming.
      - [Godbolt Compiler Explorer](https://godbolt.org/): View assembly generated from high-level languages.
    - **YouTube Tutorials**:
      - Search for beginner-friendly assembly tutorials specific to x86 or ARM.
    """)
