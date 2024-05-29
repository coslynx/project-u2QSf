class RequestSystem:
    def __init__(self):
        self.requests = []

    def send_request(self, sender, receiver, request_type):
        request = {
            'sender': sender,
            'receiver': receiver,
            'request_type': request_type
        }
        self.requests.append(request)

    def view_requests(self, trainer):
        trainer_requests = [req for req in self.requests if req['receiver'] == trainer]
        return trainer_requests

    def accept_request(self, trainer, sender, request_type):
        for req in self.requests:
            if req['receiver'] == trainer and req['sender'] == sender and req['request_type'] == request_type:
                self.requests.remove(req)
                return True
        return False

    def decline_request(self, trainer, sender, request_type):
        for req in self.requests:
            if req['receiver'] == trainer and req['sender'] == sender and req['request_type'] == request_type:
                self.requests.remove(req)
                return True
        return False
