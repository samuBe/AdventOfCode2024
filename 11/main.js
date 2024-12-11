
function transform(stone){
    if (stone === 0){
        return [1]
    }
    const string_stone = stone.toString()
    if (string_stone.length % 2 === 0){
        const mid = Math.floor(string_stone.length / 2)
        return [Number(string_stone.slice(0,mid)), Number(string_stone.slice(mid))]
    }
    return [stone * 2024]
}

const path = "input.txt";
const file = Bun.file(path);

const text = await file.text();
let stones = text.split(' ').map((s)=>Number(s))

for (let i=0; i<75;i++){
    console.log(i)
    let temp = []
    for (const stone of stones){
        let ans = transform(stone)
        temp = temp.concat(ans)
    }
    stones = temp
}

console.log(stones.length)
