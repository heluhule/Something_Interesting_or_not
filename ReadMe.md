# WriteUp for reversing.kr

## A short write up to note down what I learned.

### Tools used:
1. X32dbg
2. Ollydbg


## Problem 1: Easy_Crack_Me

This is a simple exe file to check whether the password is true or not.
<p align="center">
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/21a9ec86-7f14-4d66-b15f-27d66e07875a" alt="image" width="500">
</p>
This is big hint, just track it down from the string "Incorrect Password" using x32dbg:

<p align="center">
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/e1f13031-10f3-4ae3-a2d9-71a329143dd6" alt="image" width="500">
</p>

Disassemble I saw the file is trying to compare (cmp) what I typed in with the correct answer. If it is not the same, it will jump to easy_crackme.401135 by using **jne**. So I just make it **je** instead of **jne** to reverse the algorithm:

<p align="center">
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/15979da9-b02c-4036-8f9f-b46ec849a0a8" alt="image" width="500"> 
</p>

I got the true notification there without looking for the password. However the password is right here, in the comparing part we can see that the code is trying to compare my input with "a", "5y", "R3versing" and "E". Then look at the stack to get the true order we can see that the password here is:

### 5yR3versing

<p align="center">
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/10482e2a-c89a-48bb-b557-20d415008972" alt="image" width="500"> 
</p>


## Problem 2: Easy_KeyGen

**Method 1: Crack without knowing the password**

Another simple file to check input. First try with random thing, the output is **Wrong** so we can track from this info. 
Disassemble I saw that the code try to hide the value input is being compare, however, in the last final it compare the return value of the compare function with a set value to print out the answer. This mean I can get the correct notification by changing from **jne** to **je** and I got the answer:

<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/9e448e09-6fae-4b01-85ad-07028099e66e" alt="image" width="500"> 
</p>


This method easy very easy as I understood the code. However I did not get the password so I will do another method to get the password.


**Method 2: Get the password**




