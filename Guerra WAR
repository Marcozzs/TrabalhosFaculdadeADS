#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
    Programa: WAR Estruturado - Missões Estratégicas
    Objetivo: Implementar missões dinâmicas para jogadores, com sorteio,
              ataque entre territórios e verificação automática de vitória.
    Autor: [Seu Nome]
*/

// ==== Estrutura de dados ====
typedef struct {
    char nome[30];  // Nome do território
    char cor[10];   // Cor do exército
    int tropas;     // Quantidade de tropas
} Territorio;

// ==== Declaração de funções ====
void cadastrarTerritorios(Territorio* mapa, int quantidade);
void exibirTerritorios(Territorio* mapa, int quantidade);
void atacar(Territorio* atacante, Territorio* defensor);
void atribuirMissao(char* destino, char* missoes[], int totalMissoes);
int verificarMissao(char* missao, Territorio* mapa, int tamanho);
void liberarMemoria(Territorio* mapa, char* missaoJogador);

// ==== Função principal ====
int main() {
    srand(time(NULL));

    int quantidade;
    printf("Digite o número de territórios a serem cadastrados: ");
    scanf("%d", &quantidade);

    // Alocação dinâmica de territórios
    Territorio* mapa = (Territorio*) calloc(quantidade, sizeof(Territorio));
    if (mapa == NULL) {
        printf("Erro ao alocar memória para territórios!\n");
        return 1;
    }

    cadastrarTerritorios(mapa, quantidade);
    exibirTerritorios(mapa, quantidade);

    // === MISSÕES ===
    char* missoes[] = {
        "Conquistar 3 territórios consecutivos",
        "Eliminar todas as tropas da cor vermelha",
        "Conquistar pelo menos 2 territórios da cor azul",
        "Ter 3 territórios com mais de 5 tropas",
        "Dominar todos os territórios de uma única cor inimiga"
    };
    int totalMissoes = sizeof(missoes) / sizeof(missoes[0]);

    // Aloca espaço para missão do jogador
    char* missaoJogador = (char*) malloc(100 * sizeof(char));
    if (missaoJogador == NULL) {
        printf("Erro ao alocar memória para a missão!\n");
        free(mapa);
        return 1;
    }

    atribuirMissao(missaoJogador, missoes, totalMissoes);
    printf("\n🎯 Sua missão secreta: %s\n", missaoJogador);

    // === LOOP DE JOGO ===
    char continuar = 's';
    while (continuar == 's' || continuar == 'S') {
        int idAtacante, idDefensor;

        printf("\nEscolha o número do território atacante: ");
        scanf("%d", &idAtacante);
        printf("Escolha o número do território defensor: ");
        scanf("%d", &idDefensor);

        if (idAtacante < 1 || idAtacante > quantidade ||
            idDefensor < 1 || idDefensor > quantidade) {
            printf("❌ Índice inválido! Tente novamente.\n");
            continue;
        }

        atacar(&mapa[idAtacante - 1], &mapa[idDefensor - 1]);
        exibirTerritorios(mapa, quantidade);

        // Verificação automática da missão
        if (verificarMissao(missaoJogador, mapa, quantidade)) {
            printf("\n🏆 MISSÃO CUMPRIDA! VOCÊ VENCEU O JOGO!\n");
            break;
        }

        printf("\nDeseja realizar outro ataque? (s/n): ");
        scanf(" %c", &continuar);
    }

    liberarMemoria(mapa, missaoJogador);
    printf("Programa encerrado.\n");

    return 0;
}

// ==== Funções auxiliares ====

// Função de cadastro
void cadastrarTerritorios(Territorio* mapa, int quantidade) {
    for (int i = 0; i < quantidade; i++) {
        printf("\n=== Cadastro do %dº Território ===\n", i + 1);

        printf("Digite o nome do território: ");
        scanf(" %[^\n]", mapa[i].nome);

        printf("Digite a cor do exército: ");
        scanf(" %[^\n]", mapa[i].cor);

        printf("Digite a quantidade de tropas: ");
        scanf("%d", &mapa[i].tropas);
    }
}

// Função de exibição
void exibirTerritorios(Territorio* mapa, int quantidade) {
    printf("\n===== ESTADO ATUAL DOS TERRITÓRIOS =====\n");
    for (int i = 0; i < quantidade; i++) {
        printf("\nTerritório %d:\n", i + 1);
        printf("Nome: %s\n", mapa[i].nome);
        printf("Cor: %s\n", mapa[i].cor);
        printf("Tropas: %d\n", mapa[i].tropas);
    }
    printf("=========================================\n");
}

// Função de ataque com rolagem de dados
void atacar(Territorio* atacante, Territorio* defensor) {
    printf("\n⚔️  %s (%s) está atacando %s (%s)!\n",
           atacante->nome, atacante->cor, defensor->nome, defensor->cor);

    if (strcmp(atacante->cor, defensor->cor) == 0) {
        printf("❌ Erro: você não pode atacar um território da mesma cor!\n");
        return;
    }

    if (atacante->tropas <= 1) {
        printf("❌ O território atacante precisa ter mais de 1 tropa para atacar!\n");
        return;
    }

    int dadoAtacante = rand() % 6 + 1;
    int dadoDefensor = rand() % 6 + 1;

    printf("🎲 Dado atacante: %d | 🎲 Dado defensor: %d\n", dadoAtacante, dadoDefensor);

    if (dadoAtacante > dadoDefensor) {
        printf("🏆 %s conquistou %s!\n", atacante->nome, defensor->nome);
        strcpy(defensor->cor, atacante->cor);
        defensor->tropas = atacante->tropas / 2;
        atacante->tropas -= defensor->tropas;
    } else {
        printf("💥 %s resistiu ao ataque!\n", defensor->nome);
        atacante->tropas--;
    }
}

// Função que sorteia uma missão aleatória
void atribuirMissao(char* destino, char* missoes[], int totalMissoes) {
    int indice = rand() % totalMissoes;
    strcpy(destino, missoes[indice]);
}

// Função que verifica se a missão foi cumprida
int verificarMissao(char* missao, Territorio* mapa, int tamanho) {
    // Lógica simplificada de exemplo:
    if (strstr(missao, "3 territórios consecutivos") != NULL) {
        // Verifica se há 3 territórios da mesma cor seguidos
        int consecutivos = 1;
        for (int i = 1; i < tamanho; i++) {
            if (strcmp(mapa[i].cor, mapa[i - 1].cor) == 0)
                consecutivos++;
            else
                consecutivos = 1;
            if (consecutivos >= 3)
                return 1;
        }
    }
    else if (strstr(missao, "vermelha") != NULL) {
        // Verifica se ainda existem territórios vermelhos
        for (int i = 0; i < tamanho; i++) {
            if (strcmp(mapa[i].cor, "vermelha") == 0)
                return 0; // ainda há inimigos
        }
        return 1; // todos eliminados
    }
    else if (strstr(missao, "mais de 5 tropas") != NULL) {
        int conta = 0;
        for (int i = 0; i < tamanho; i++) {
            if (mapa[i].tropas > 5)
                conta++;
        }
        if (conta >= 3)
            return 1;
    }

    // Missão ainda não cumprida
    return 0;
}

// Função para liberar memória
void liberarMemoria(Territorio* mapa, char* missaoJogador) {
    free(mapa);
    free(missaoJogador);
    printf("\n🧹 Memória liberada com sucesso!\n");
}
