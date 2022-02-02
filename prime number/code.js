const t = parseInt(prompt())

for (let i = 0; i < t; i++) {
    let n = parseInt(prompt())
          
    let count = 0;
    for (let div = 2; div * div <= n; div++) {
        if (n % div == 0) {
            count++;
            break;
        }

    }

    if (count == 0) {
        System.out.println("prime");
    } else {
        System.out.println("not prime");
    }
}