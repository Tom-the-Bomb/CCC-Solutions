use std::{
    io,
    collections::{HashSet, VecDeque},
};

fn main() {
    let stdin = io::stdin();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)
        .unwrap();
    let m = buffer
        .trim()
        .parse::<usize>()
        .unwrap();

    buffer.clear();
    stdin.read_line(&mut buffer)
        .unwrap();

    let n = buffer
        .trim()
        .parse::<usize>()
        .unwrap();

    let grid = (0..m)
        .map(|_| {
            buffer.clear();
            stdin.read_line(&mut buffer)
                .unwrap();

            buffer
                .split_whitespace()
                .filter_map(|x| x.trim().parse::<usize>().ok())
                .collect::<Vec<usize>>()
        })
        .collect::<Vec<Vec<usize>>>();

    let mut seen = HashSet::new();
    let mut queue =  VecDeque::from([(1, 1)]);

    while let Some((row, col)) = queue.pop_front() {

        for i in 1..=m {
            for j in 1..=n {
                let coords = (i, j);

                if i * j == grid[row - 1][col - 1]
                    && !seen.contains(&coords)
                {
                    if i == m && j == n {
                        println!("yes");
                        return;
                    }

                    queue.push_back(coords);
                    seen.insert(coords);
                }
            }
        }
    }
    println!("no");
}