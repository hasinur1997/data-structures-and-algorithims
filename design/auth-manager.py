class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.expaire_at = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.expaire_at

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] >= currentTime:
            self.tokens[tokenId] = currentTime + self.expaire_at

    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter = 0

        for item in self.tokens:
            if self.tokens[item] > currentTime:
                counter += 1

        return counter


auth = AuthenticationManager(5)
auth.renew('aaa', 1)
auth.generate('aaa', 2)
auth.generate('bbb', 7)
auth.renew('aaa', 8)
auth.renew('bbb', 10)
print(auth.countUnexpiredTokens(15))

print(auth.tokens)