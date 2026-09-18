# insta-follower

Interactive social challenge website.

## Creator credits / payments

A separate `payments.html` page has been added as a **demo wallet** for legitimate creator tools or digital services. It intentionally does not process real money.

For a real payment flow:

1. User selects a credit package.
2. Frontend asks your backend to create a payment order.
3. Backend creates the order with a payment provider.
4. Frontend opens the provider checkout.
5. Provider confirms the payment.
6. Backend verifies the payment signature/webhook.
7. Backend records the transaction and credits the user's account.
8. The frontend reads the balance from the backend.

Do not put payment-provider secret keys in this GitHub Pages frontend.

The payment system should only be used for clearly described, legitimate products/services and should not represent simulated follower rewards as guaranteed real Instagram growth.
