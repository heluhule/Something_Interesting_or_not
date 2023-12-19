### EasyKeyGen3

Another Keygen problem here. Let see what we have through IDA: 

<p align="center">
  
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/42fb8438-30f3-4349-bce0-d2713ffe0d75" alt="image" width="500"> 
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/fa568a31-f96a-4433-816c-5b206764fa74" alt="image" width="500"> 

</p>

Ok so we have some simple things here. So it will get text by **GetDlgItemTextA()** then compare the length with 3 and 35 (23h) --> this must be the length restriction. As I understand, Name should be > 3 characters, and Serial must exactly 35 characters. What's more, we can see that it compares the character to "-" every 8 character, so I guess it can be the form of 32 Serial numbers with - every 8 ones: 

<p align="center">
########-########-########-########

</p>
Let me try:

<p align="center">

<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/0f7172b5-e04c-4de1-a224-ee5002309df6" alt="Image 1" width="350">
<br> Wrong format

</p>

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/5f47261a-7e1e-4075-bc4c-2b25f045aefa" alt="Image 2" width="350">
<br>My read is true
</p>

Now let see what is FirstSerialCheck and SecondSerialCheck. One last glance before running it with debugger, this is also interesting:


<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/52956d9d-d035-4672-a665-6c78e1465a34" alt="Image 1" width="200">
</p>

**_strcpy()** is used 4 times, which may mean that this divides Serial into 4 parts and does something with it. This could be the SerialCheck I'm looking for so I set some breakpoints here, let see what we may have in X32DBG: 

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/e0f438b2-71ff-4512-8a65-e11a4f315fc5" alt="Image 1" width="500">
</p>

After having copied the FirstSerial, it will be transfered to signed 32bit Hexa value as in the box of the middle I showed, then it will divided by 1000000 and store the value in the FPU stack. The same process will be applied to all the Serials. After this process, we will enter the FirstSerialChecking process. 

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/1b178d8d-a53e-4e15-b9d0-b4648658c6ce" alt="Image 2" width="550">
<br>Serial changed for better vision
</p>
As I labeled in the debugger, overall the First Serial Checking will belike: 
<p align="center"> 65535.998 < (LastSerial)<sup>2</sup> + (SecondSerial)<sup>2</sup> < 65536.002 </p>
<p align="center"> 65535.998 < (FirstSerial)<sup>2</sup> + (ThirdSerial)<sup>2</sup> < 65536.002 </p>


#### Note  These values are after divided by 1000000, and *Serial here should be float numbers.

Ok now let me check my read again:

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/2b2af9a7-26df-47b9-8b8f-ef05ffcb7592" alt="Image 1" width="300">
  <br><strong>0F424000 here is 256000000</strong>
</p>

Good now!
<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/eaa04a3c-fc67-48ee-a49b-a301cda214f4" alt="Image 1" width="500">
</p>
I label it all in the image so we can see the the algorithm to check the Second Serial is:
<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/5720ff91-243b-4a60-bc08-104e7711c5c0" alt="Image 1" width="500">
</p>
The problem here is what [40DE3E8] and [40DE3F0] are? Nevermind just check the algorithm first (Get the [40DE3E8] and [40DE3F0] from debugger and calculation by hand to check)

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/2b2af9a7-26df-47b9-8b8f-ef05ffcb7592" alt="Image 1" width="400">
  <br><strong>Helo, World!</strong>
</p>

Alright, last part is looking for [40DE3E8] and [40DE3F0]. Back to the IDA here is the only part working with these 2 values

<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/5fd90e7a-0510-41c2-b84f-696752a587e3" alt="Image 1" width="400">
</p>

The code here is readable, first it set [40D410] is 0xFFFFFFFFh. Then loop through every character of the Name with the flow:
 - Get the ASCII value of character.
 - xor_result = ascii_value ^ [40D410]
 - and_result = xor_result & 0x000000FF
 - result_list[(and_result x 4)-4 : (and_result x 4)]
 - nextSHR = [40D410] >> 8
 - [40D410] = nextSHR ^ **combined_hex** 

*Note **combined_hex** is to get the value numbers in the list of value of [40D000]. We can see this list in IDA.*

After having the value of [40D410], it will divided into 2 parts which is higher and lower. And now it is done:
 - [40DE3E8] =  int((higher_part % 8198) + 256)
 - [40DE3F0] =  int((lower_part % 8198) + 256)

It should be done now (If my code is true). Test it:
<p align="center">
<img src="https://github.com/heluhule/Something_Interesting_or_not/assets/148317962/346670b7-f553-4f54-8f95-286f050a2d1e" alt="Image 1" width="600">
</p>

#### Surprisingly it is true.


