<script>
    import { onMount } from "svelte";
    import {fetchOffers} from '../../../../lib/data/offer'

    let items = [];

    onMount(async () => {
        items = await fetchOffers()
        
    } )
</script>

<section>
    <header>
        <h2>Последние заявки</h2>
    </header>

    <ul>
        <li class="li-header">
            <p>№ заявки</p>
            <p>Позиция</p>
            <p>Id товара</p>
            <p>Заказчик</p>
            <p>Адрес</p>
            <p>Количество </p>
        </li>
        {#each items as item, i}
            <li>
                <p>{item.supply_id}</p>
                <p>{item.product.name}</p>
                <p>{item.product.sku}</p>
                <p>{item.product.manufactor}</p>
                <p>{item.placement.address}</p>
                <p>{item.product.product_amount} {item.product.product_measure}</p>
            </li>
        {/each}
    </ul>
</section>

<style lang="scss">
    section{
        flex: 1px;
        background: var(--white);
        padding: 35px;
        border-radius: 35px;
        max-height: 27rem;
    }

    header{
        margin-bottom: 46px;
        
        h2{
            font-weight: 700;
            font-size: 30px;
            margin-bottom: 8px;
        }
    }

    ul{
        max-width: 100%;
        max-height: 50.5%;
        overflow: hidden;

        li{
            border: 1px solid var(--dark-blue-40);
            padding: 20px 0;
            display: grid;
            grid-template-columns: 130px 200px 126px 260px 195px auto;

            &:first-child{
                padding: 0 0 33px;
                border: none;
            }

            p:nth-child(1){
                padding-left: 15px;
            }

            p:nth-child(4){
                padding-right: 8px;
            }

            p:nth-child(5){
                max-width: 250px;
            }
            
            p:nth-child(6){
                text-align: center;
            }

        }
    }

</style>