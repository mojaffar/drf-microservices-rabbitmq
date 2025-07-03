from celery import shared_task

@shared_task
def notify_new_order(product_name, user_email):
    print(f"[x] Notifying {user_email} for {product_name}")