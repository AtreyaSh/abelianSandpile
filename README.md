# Abelian Sandpile Cascade Effect

## Background

The Abelian sandpile is an interesting example of a well-ordered game which leads to very interesting results, especially in the context of self-organized criticiality. Here we will experiment with the Abelian sandpile using python scripts.

The inspiration for this project was drawn from a recent [Numberphile](https://www.youtube.com/watch?v=1MtEUErz7Gg) video. Kudos to them for making mathematics so accessible to the general public!

## Algorithm with Confined Example

1. Assume the existence of the following 3x3 grid with 4 "sand grains" at the centre. The rest of the cells in the grid have a value of 0. This is illustrated below.

2. Here, we set a sand grain limit of each cell to be 4. This means that if a single cell has 4 or more sand grains, it will topple and release its sand grains in 4 directions. Since the centre cell has 4 sand grains, it will topple and release its sand grains in the following manner. After one iteration, no cell has sand grains equal to or more than 4. Therefore, the cells are in equilibrium. This is also illustrated below.

<img src="/rdimg/Visuals.png" width="500">

## Generic Algorithm

Now, assume the same sand grain limit of 4 per cell. Instead of a 3x3 grid, we assume an infinitely large grid. We also place an arbitrary number of grains `N` at the centre of the grid. Assuming N is large, we want to investigate the equilibrium state of sand grains. We apply the same algorithm as before and investigate the changes.

<img src="/rdimg/Visuals2.png" width="500">

## Visualizations

Here are two nice gifs that we made to visualize the 2-dimensional Abelian sandpile cascade effect.

1. The following animation shows the cascading effect from a fixed perspective, such that one can observe how the sandpile expands. This emphasizes holistic structural changes.

<img src="https://github.com/AtreyaSh/abelianSandpile/blob/master/gif/sandyMovie2.gif" width="500">

2. This next animation shows the cascading effect from a varying perspective, such that the sandpile is constantly in focus. This emphasizes internal structural changes.

<img src="https://github.com/AtreyaSh/abelianSandpile/blob/master/gif/sandyMovie.gif" width="500">

Math is beautiful!

## Developments

1. We hope to convert the above 2-dimensional visualization into a 3-dimensional animation. Essentially, colors will be converted into Z-type heights. This way, we will have a clearer idea of feedback cascade effects as the sandpile progresses.

2. We would like to extend an intrinsic 2-dimensional sandpile into a 3-dimensional sandpile; essentially on 3-dimensional grid. We will try to make 3-dimensional shadows of the resulting 4-dimensional results, still figuring what this means...
