<script lang="ts" context="module">
    import type { Placement } from "$lib/data/placement";
    import type { LngLat } from "@yandex/ymaps3-types";

    export type MarkerData = {
        id: number;
        kind: "storage" | "client";
        location: LngLat;
        placement: Placement;
    };

    export let selected_places = writable<number[]>([]);
</script>

<script lang="ts">
    import { writable } from "svelte/store";

    export let data: MarkerData;
    export let click: (data: MarkerData) => void = () => {};

    let path: string;
    $: {
        if ($selected_places.includes(data.id)) {
            path = "selected";
        } else if (data.kind === "storage") {
            path = "warehouse";
        } else if (data.kind === "client") {
            path = "store";
        } else {
            path = "warehouse"; // Just in case
        }
        path = `/markers/${path}.svg`;
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
    class="marker"
    data-id={data.id}
    on:click={() => {
        $selected_places = [data.id];
        click(data);
    }}
>
    <img src={path} alt="" />
</div>

<style lang="scss">
    .marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;

        width: 0;
        height: 0;

        img {
            position: absolute;
            bottom: 0;
            width: 48px;
        }
    }
</style>
