from abc import ABC, abstractmethod


class Tags(ABC):
    @abstractmethod
    def get_front_tag(self):
        pass

    @abstractmethod
    def get_back_tag(self):
        pass


class MyMLTag(Tags):
    def get_front_tag(self):
        return "<MyML>"

    def get_back_tag(self):
        return "</MyML>"


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self, front_tag, end_tag):
        pass


class MyContent(IContent):
    def format(self, front_tag, end_tag):
        return f"{front_tag}{self.text}{end_tag}"


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content, front_tag, back_tag):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.sender = None
        self.receiver = None
        self.content = None

    @property
    def protocols(self):
        return {"IM": "I'm"}

    def set_sender(self, sender):
        if self.protocol in self.protocols:
            self.sender = f"{self.protocols[self.protocol]} {sender}"
        else:
            self.sender = sender

    def set_receiver(self, receiver):
        if self.protocol in self.protocols:
            self.receiver = f"{self.protocols[self.protocol]} {receiver}"
        else:
            self.receiver = receiver

    def set_content(self, content, front_tag, back_tag):
        self.content = content.format(front_tag, back_tag)

    def __repr__(self):
        return f"Sender: {self.sender}\nReceiver: {self.receiver}\nContent:\n{self.content}"


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
ml_tags = MyMLTag()
email.set_content(content, ml_tags.get_front_tag(), ml_tags.get_back_tag())
print(email)
