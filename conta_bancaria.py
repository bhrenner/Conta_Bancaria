class conta:
    def __init__(self, nome, saldo, banco, numero):
        self.nome = nome
        self.saldo = saldo
        self.banco = banco
        self.numero = numero
        pass

    def __str__(self):
        return f'\nTitular: {self.nome} --- {self.banco} \nConta: {self.numero} --> Saldo: R${self.saldo}'
        pass

    def transferencia(self, valor, cont):
        if self.banco == 'Bradesco':
            taxa = (int(valor) * 0.005) + 5
            soma = taxa + valor
            if cont.nome != self.nome:
                if soma >= self.saldo:
                    return f'Você não possui saldo sulficiente para essa transação!'
                else:
                    self.saldo = self.saldo - soma
                    cont.saldo = cont.saldo + valor
                    return f'Titular: {self.nome} --> Valor da transferencia(com taxas): {soma} \nSaldo atual {self.saldo}\nTranferência concluída para {cont.nome} saldo: {cont.saldo}!'
            elif cont.nome == self.nome or cont not in conta:
                return f'Não foi possivel fazer o processo, verifique os dados!'
        elif self.banco == 'Itau':
            taxa = int(valor) * 0.01
            soma = taxa + valor
            if cont.nome != self.nome:
                if soma >= self.saldo:
                    return f'Você não possui saldo sulficiente para essa transação!'
                else:
                    self.saldo = self.saldo - soma
                    cont.saldo = cont.saldo + valor
                    return f'Titular: {self.nome} --> Valor da transferencia(com taxas): {soma} \nSaldo atual {self.saldo}\nTranferêcia concluída para {cont.nome} saldo: {cont.saldo}!'
            elif cont.nome == self.nome or cont not in conta:
                return f'Não foi possivel fazer o processo, verifique os dados'
        else:
            return f'Banco não faz parte, processo não é permitido!!!'

ana = conta('Ana', 1000, 'Bradesco', '001')
joao = conta('João', 500, 'Itau', '002')
lais = conta('Lais', 100, 'Santander', '003')
jose = conta('José', 3000, 'Bradesco', '004')
maria = conta('Maria', 90, 'Itau', '005')

print(ana, joao, lais, jose, maria)
print('-' *50)
print(ana.transferencia(100, ana))
print('-' *50)
print(ana.transferencia(100, lais))
print('-' *50)
print(joao.transferencia(150,ana))
print('-' *50)
print(jose.transferencia(1500,maria))
print('-' *50)
print(maria.transferencia(50, joao))
print('-' *50)
print(lais.transferencia(50, joao))
print('-' *50)
print(maria.transferencia(5000, joao))
