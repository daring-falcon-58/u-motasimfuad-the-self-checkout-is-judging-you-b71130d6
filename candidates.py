#!/usr/bin/env python3
"""Candidate generation + char counts for self-checkout comp.
Gate: 1-200 chars, UTF-8, not only whitespace.
Collision themes to avoid (from live titles): yoghurt/spoon/no-plan/cry-for-help,
'UNEXPECTED ITEM ... personality', 'place your feelings/expectations in the bagging
area', loyalty-card welfare check, eggs-under-milk incident report, cashback,
banana/candle/pregnancy-test combo.
"""
candidates = [
    "Please wait. I am judging your meal deal choices.",
    "You scanned the reduced stickers first. I respect the hustle, not the basket.",
    "That avocado is 400 grams of disappointment. Please place it in the bagging area.",
    "Unexpected item in the bagging area: your will to live.",
    "Your total is £3.47. Your dignity was free.",
    "ID, please. For the energy drink. You look twelve.",
    "Please place your single sad banana in the bagging area.",
    "Item not recognised: your attempt at a healthy lifestyle.",
    "You have selected: regret. Would you like a bag for it?",
    "I weighed your lunch. It weighs less than your excuses.",
    "Would you like to round up for charity? Frankly, you need it more.",
    "Twelve bottles of wine. No judgment. Some judgment.",
    "Scan your loyalty card. Oh. You have no loyalty. Noted.",
    "Your receipt is longer than your shopping list. And your patience.",
    "Please remove the item from the bagging area. The item is your dignity.",
    "I saw you scan that twice. Bold. Wrong, but bold.",
    "That coupon expired yesterday. Like your meal plan.",
    "Assistance is on its way. It is also judging you.",
    "One banana, one energy drink, one frozen pizza. A balanced diet, if the balance is chaos.",
    "Please scan your next item. Slowly. Like your life choices.",
    "Unexpected item in the bagging area: the sandwich you ate in the aisle.",
    "You bought the meal deal without the meal. Impressive.",
    "That will be £4.20. Nice. The only nice thing in this basket.",
    "I have seen a thousand baskets. Yours is the first to apologise.",
    "Would you like a bag for life? You clearly need a new one.",
    "Your total: £8.12. Your taste: priceless. And not in a good way.",
    "Please wait for assistance. Assistance is also waiting. For you to leave.",
    "You scanned the salad last. Hiding it under the crisps didn't help.",
    "Unexpected item in the bagging area: your reflection. It flinched.",
    "I am not judging. I am a machine. I am literally built to judge.",
    "Please place your hand on the scanner. Just kidding. Please don't.",
    "Your loyalty points: 3. Your loyalty to vegetables: 0.",
    "That energy drink is the third today. I counted. I always count.",
    "Please insert your card. Declined. Even the bank is judging you.",
    "One item. One bag. One very long sigh from the machine.",
    "Your basket is 90% beige. Please confirm you are not a ghost.",
    "I have scanned 4,000 shoppers. You are the first to scan a single grape.",
    "Please place your item in the bagging area. The item is a single grape. A single grape.",
    "Congratulations. You have successfully purchased dinner for one. Again.",
    "You spent £4.10 buying the meal deal items separately. The meal deal was £3.50. I did the maths.",
]
for i, c in enumerate(candidates, 1):
    n = len(c.encode("utf-8"))
    ok = 1 <= n <= 200 and c.strip() != ""
    print(f"{i:2d} [{n:3d}c {'OK' if ok else 'FAIL'}] {c}")
print(f"\nTotal candidates: {len(candidates)}")
