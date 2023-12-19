# WriteUp for everything I found interesting

## A short write up to note down what I learned.

### Tools used:
1. X32dbg
2. Ollydbg
3. IDA


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

Look at these 3 lines we can see that this is building an array with 0x10h, 0x20h, 0x30h
<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/8fdf19e4-b8af-4e77-b8c9-f636f769d660" alt="image" width="500"> 
</p>

Now input some random things and we have this:

<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/345f9065-4c8d-4e75-871b-d4e388120978" alt="image" width="500"> 
</p>

Look at the right corner, we can see that we have number "21". So how do we get this? Back to the array, the first is 0x10, and the first character in the input is 1 ( 1 in ascii is 31) this is XOR encryption. Do one more loop to assure my thinking is true:

<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/855f7b38-8a19-4794-ab0a-f6456be17f0f" alt="image" width="500"> 
</p>

Now we have 0x12 as we thought so it seems true. Do some code to get the true input from given serial:   
<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/bb550ea0-e7d2-4af3-ab3f-b2d02e13242b" alt="image" width="500"> 
</p>

### K3yg3nm3

**Method 3: Easy_UnpackMe**

This is kinda simpler problem than I thought. Run for the first try, notice that it directly jump to the location: 00401150.
<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/b95789a0-2da0-4351-8e75-56f779620d16" alt="image" width="500"> 
</p>

Submit the number and it is true:

<p align="center">
  
<img src="https://github.com/heluhule/Write-Up-for-reversing.kr/assets/148317962/dfcfb5be-52da-4037-ae04-7a44004be59b" alt="image" width="500"> 
</p>

### 00401150


## Replace
At first I was a little bit confusing since just do not know what to do. Throw it into IDA so I can see that there is "nothing" lead me to the flag, so I should find that nothing right?

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/dc69d4a6-b91c-42bd-8c13-91c7f1026cc8" alt="image" width="500"> 
</p>

Get the flow of the code so let see what is happening. After trying from 0 to 10, I have realized something here:
<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/be5235c7-202d-4b68-b4c3-00a68a4f9e24" alt="image" width="500"> 
  <br>Input = 0
</p>

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/8ac1f6ab-33e8-4818-a6ee-0c690b2c52a0" alt="image" width="500"> 
  <br>Input = 5
</p>

Something pop up in my mind. The only parameter pushed while calling loc_404689 is changed, and the result the function is **mov byte ptr ds:[eax], 90**. At first I was stuck with pushing a hexa value into eax, but it seems not that. 90 is OP CODE for NOP here, which means the program is trying to overwrite some OP CODE to lead us to the flag. The only OP CODE should be overwritten is **loc_401071** since it denies us to reach the flag. So now, the problem is clear that we have to find out the suitable number to get **loc_401071**. Run some more, I found that the first parameter is like:
<p align="center">
**EAX = 0x601605D7 + 4 + Input** ---> **0x00401071 = 0x601605D7 + 4 + Input**
</p>
Since we can input nothing but integer, make sure to add a 1 into **0x00401071** to get a positive value by overflow. Now the key is
<p align="center" >
  **Input = 0x100401071 - 0x601605D7 - 4 = 2687109798**
</p>

