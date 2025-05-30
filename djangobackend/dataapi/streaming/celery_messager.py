from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_message_from_socket():
    channel_layer = get_channel_layer()
    message = "Hello from Celery!"

    # Send a message to the WebSocket group
    async_to_sync(channel_layer.group_send)(
        'data_websocket_group',  # The group name used in your WebSocket consumer
        {
            'type': 'send_message',  # This should match the method in your WebSocket consumer
            'message': message,
        }
    )

    return {
        'type': 'send_message',  # This should match the method in your WebSocket consumer
        'message': message,
    }