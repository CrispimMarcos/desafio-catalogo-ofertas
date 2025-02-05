import React, { useState, useEffect } from 'react';
import './ProductList.css'; // Arquivo CSS para estilizar os produtos

function ProductList() {
    const [produtos, setProdutos] = useState([]);

    useEffect(() => {
        fetch('/produtos/')
            .then(response => response.json())
            .then(data => {
                console.log(data); // Adicione este log
                setProdutos(data);
            });
    }, []);

    return (
        <div className="product-list">
            <h1>Produtos Encontrados</h1>
            <div className="filters">
                <h2>Opções de Filtro:</h2>
                <form method="GET">
                    <label>
                        <input type="checkbox" name="frete_gratis" /> Frete Grátis
                    </label>
                    <label>
                        <input type="checkbox" name="full" /> Full
                    </label>
                    <button type="submit">Filtrar</button>
                </form>
            </div>
            <div className="products">
                {produtos.map(produto => (
                    <div key={produto.id} className="product-item">
                        <img src={produto.imagem} alt={produto.nome} />
                        <p>{produto.nome}</p>
                        <p>Preço: {produto.preco}</p>
                        <p>Parcelamento: {produto.parcelamento}</p>
                        <a href={produto.link}>Ver Produto</a>
                        {produto.preco_sem_desconto && <p>Preço sem Desconto: {produto.preco_sem_desconto}</p>}
                        {produto.percentual_desconto && <p>Desconto: {produto.percentual_desconto}%</p>}
                        <p>Tipo de Entrega: {produto.tipo_entrega}</p>
                        {produto.frete_gratis && <p>Frete Grátis</p>}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ProductList;
