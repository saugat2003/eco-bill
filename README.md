# Eco-Bill

Eco-Bill is a web application that helps businesses create invoices online and send them directly via email or WhatsApp. Built entirely with Django, Eco-Bill promotes sustainability by reducing paper waste and streamlining invoicing processes digitally.

## Features
- **Online Invoice Creation** – Generate invoices quickly and efficiently.
- **Email / WhatsApp Integration** – Send invoices directly to clients.
- **Sustainability Focus** – Supports paperless invoicing for an eco-friendly approach.
- **User Authentication** – Secure login and user management.
- **Invoice History** – Keep track of past invoices.
- **Customizable Templates** – Personalize invoices with company branding.
- **PDF Export** – Download invoices in PDF format.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **APIs:** SMTP for email

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/saugat2003/eco-bill.git
   cd eco-bill
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables (`.env` file):
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   EMAIL_HOST=your_email_host
   WHATSAPP_API_KEY=your_whatsapp_api_key
   ```
5. Run database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the app at `http://127.0.0.1:8000/`.

## Usage
1. Sign up or log in to your account.
2. Create a new invoice by entering customer and product details.
3. Preview and customize your invoice.
4. Send the invoice via email or WhatsApp with a single click.
5. Track all invoices in your dashboard.

## Contributing
Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch (`feature-branch`).
- Commit your changes.
- Push to your fork and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, reach out at [saugat.codes@gmail.com].

![Screenshot 2025-02-11 061224](https://github.com/user-attachments/assets/a1413dfd-6bac-4488-ba5f-c34a609b5507)
![Screenshot 2025-02-11 061208](https://github.com/user-attachments/assets/8c369b5e-3d2b-454a-ae9b-46d7ad90a9c2)
![Screenshot 2025-02-11 061126](https://github.com/user-attachments/assets/37da545e-5c21-4fb4-9a6d-d69d04b39ed2)
