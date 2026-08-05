# Problem Statement

## 1. Title
Gift Card & Voucher Management System

## 2. Domain
FinTech / Retail-Tech — digital gift card and promotional voucher issuance, purchase, and redemption.

## 3. Who is the user? (2-3 user types, with roles)
- **Admin** — manages merchants, gift card templates, voucher campaigns, and oversees all transactions.
- **Merchant/Vendor** — creates voucher/discount campaigns for their store, views redemption reports for their own vouchers.
- **Customer** — buys gift cards, receives/redeems vouchers, checks balance and redemption history.

## 4. What problem are we solving? (3-5 sentences, real-life example)
Small and mid-sized retailers struggle to run their own digital gift card or voucher programs because
building one in-house is expensive, and third-party platforms charge high commissions. Customers, on the
other hand, often lose paper vouchers or forget expiry dates, leading to unused value. For example, a
customer buys a ₹500 gift card for a friend's birthday from a boutique store — today this likely means a
printed card that can be lost, whereas a digital system lets it be issued instantly, tracked, and redeemed
at checkout with a code or QR scan. This system gives merchants a lightweight platform to issue and track
gift cards and vouchers digitally, while giving customers a reliable way to buy, hold, and redeem them.

## 5. Proposed Solution (what the application will do, feature-wise)
- Admin can onboard merchants and manage system-wide gift card templates.
- Merchants can create voucher campaigns (e.g. "20% off, valid till Aug 31") with usage limits and expiry.
- Customers can browse and purchase gift cards (via a payment sandbox), each generating a unique code.
- Customers can redeem gift cards/vouchers at checkout using a code or QR, with balance auto-updating.
- Email notification sent on purchase and before expiry (via 3rd-party email service).
- Dashboards: Admin sees platform-wide analytics; Merchant sees their campaign performance; Customer sees
  their wallet (active cards/vouchers + redemption history).
- Partial redemption support for gift cards (e.g. use ₹200 of a ₹500 card, ₹300 remains).

## 6. Core Entities / Database Tables (list all, minimum 5)
1. **User** (id, name, email, password_hash, role)
2. **Merchant** (id, user_id FK, store_name, category, status)
3. **GiftCard** (id, code, initial_value, balance, issued_to_user_id FK, purchased_by_user_id FK, status, expiry_date)
4. **Voucher** (id, code, merchant_id FK, discount_type, discount_value, usage_limit, times_used, expiry_date)
5. **Transaction** (id, user_id FK, gift_card_id FK nullable, amount, payment_status, payment_gateway_ref, created_at)
6. **Redemption** (id, user_id FK, gift_card_id FK nullable, voucher_id FK nullable, amount_redeemed, redeemed_at)

## 7. User Roles & Permissions (minimum 2 distinct roles, e.g. Admin & User)
- **Admin**: full access — manage merchants, view/void any gift card or voucher, view all transactions.
- **Merchant**: create/edit/deactivate own vouchers, view own redemption reports only.
- **Customer**: purchase gift cards, redeem gift cards/vouchers, view own wallet and history only.

## 8. Success Criteria
- A customer should be able to purchase a gift card and receive a redeemable code in under 1 minute.
- A merchant should be able to create a new voucher campaign in under 2 minutes.
- Redemption (code entry to balance update) should complete in under 5 seconds.

## 9. Out of Scope (clearly list what you will NOT build, to avoid over-commitment)
- Physical/plastic card printing or POS hardware integration.
- Multi-currency support.
- Real payment processing (a payment gateway **sandbox/test mode** only — no real money moves).
- Native mobile apps (web-responsive only).

## 10. Chosen Track: Python (Django REST Framework)