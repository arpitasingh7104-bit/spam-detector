import random, csv
random.seed(7)
spam_t = [
 "WINNER!! You have won a {p} gift card. Click {l} to claim your prize now",
 "Congratulations! You've been selected for a free {p} voucher. Reply YES to claim",
 "URGENT: Your bank account is blocked. Verify your details at {l} immediately",
 "Free entry in our weekly draw to win {p} cash. Text WIN to 80085 now",
 "You have been pre-approved for a loan of {p}. No documents needed. Apply at {l}",
 "Limited offer! Buy 1 get 3 free. Order now at {l} before midnight",
 "Your parcel is on hold. Pay a small fee of Rs 49 at {l} to release it",
 "Earn {p} per day working from home. No experience needed. Click {l}",
 "Dear customer, your KYC has expired. Update now at {l} or your account will be closed",
 "Claim your free iPhone now! Only 5 left. Visit {l}",
 "Hot singles in your area want to meet you. Click {l} to chat free",
 "Lucky draw alert! Your number won {p}. Call 09061701461 to claim",
 "Get 90% off on all products today only. Shop now at {l}",
 "Final notice: you owe unpaid tax. Pay immediately at {l} to avoid arrest",
 "Double your money in 24 hours guaranteed. Invest now {l}",
 "Win a free holiday to Goa! Text HOLIDAY to 56789. T&Cs apply",
 "Your electricity will be cut tonight. Call 9876500000 and pay the bill now",
 "Exclusive deal just for you: cheap meds without prescription at {l}",
 "You are our lucky winner of {p}! Send your bank details to receive the money",
 "Congrats! Your SIM won a lottery of {p}. Contact our agent now",
]
ham_t = [
 "Hey, are you coming to class tomorrow?",
 "Can you send me the notes from today's lecture?",
 "I'll be home by 7, do you want me to bring dinner?",
 "Happy birthday! Hope you have an amazing day",
 "Meeting is moved to 3 pm, please check the calendar",
 "Did you finish the assignment? I'm stuck on question 4",
 "Mom said to call her when you reach the hostel",
 "Let's study together at the library this evening",
 "Thanks for helping me yesterday, really appreciate it",
 "The internship report is due on Friday, don't forget",
 "I'm running late, will reach in 15 minutes",
 "What time does the movie start tonight?",
 "Please share the project link on the group",
 "Good morning! Have a great day ahead",
 "Can we reschedule our call to tomorrow morning?",
 "I booked the train tickets for Saturday",
 "Lunch at the canteen at 1? Let me know",
 "Your order has been delivered. Thank you for shopping with us",
 "Your OTP for login is 482910. Do not share it with anyone",
 "Reminder: your dentist appointment is on Monday at 10 am",
 "Sorry, I missed your call. I was in a meeting",
 "Can you review my code before I push it to GitHub?",
 "The exam timetable is out, check the college portal",
 "Don't forget to carry your ID card tomorrow",
 "I'm at the bus stop, where are you?",
]
p = ["$1000", "Rs 50000", "$500", "Rs 10 lakh", "$2000", "Rs 25000"]
l = ["bit.ly/win123", "http://claim-prize.xyz", "www.free-offer.top",
     "http://secure-bank-verify.info", "tinyurl.com/gift99", "http://cash-now.click"]
rows = []
for t in spam_t:
    for _ in range(6):
        rows.append(("spam", t.format(p=random.choice(p), l=random.choice(l))))
for t in ham_t:
    for _ in range(5):
        pre = random.choice(["", "", "Hi, ", "Hey! ", "Ok, "])
        rows.append(("ham", pre + t))
rows = list(dict.fromkeys(rows))
random.shuffle(rows)
with open("spam.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["label", "message"])
    w.writerows(rows)
print(len(rows), "rows saved to spam.csv")