#include <SDL2/SDL.h>
#include <SDL2/SDL2_gfxPrimitives.h>
#include <math.h>
#include <stdbool.h>

#define WIDTH 800
#define HEIGHT 600
#define NUM_RAYS 1000
#define MAX_DIST 1000
#define STEP 1

int main(int argc, char *argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
        return 1;
    }

    // Create a high-DPI aware window
    SDL_Window *window = SDL_CreateWindow(
        "Ray Tracing Simulator",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        WIDTH, HEIGHT,
        SDL_WINDOW_ALLOW_HIGHDPI
    );
    if (!window) {
        SDL_Log("Could not create window: %s", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        SDL_Log("Could not create renderer: %s", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Adjust for high-DPI displays
    int drawableW, drawableH;
    SDL_GetRendererOutputSize(renderer, &drawableW, &drawableH);
    float scaleX = (float)drawableW / WIDTH;
    float scaleY = (float)drawableH / HEIGHT;
    SDL_RenderSetScale(renderer, scaleX, scaleY);

    float lightX = WIDTH / 2.0f;
    float lightY = HEIGHT / 2.0f;
    SDL_Rect block = { WIDTH / 4, HEIGHT / 4, 100, 100 };

    bool running = true;
    SDL_Event event;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            } else if (event.type == SDL_KEYDOWN) {
                switch (event.key.keysym.sym) {
                    case SDLK_ESCAPE:
                        running = false;
                        break;
                    // Move light source with arrow keys
                    case SDLK_UP:    lightY -= 5; break;
                    case SDLK_DOWN:  lightY += 5; break;
                    case SDLK_LEFT:  lightX -= 5; break;
                    case SDLK_RIGHT: lightX += 5; break;
                    // Move blocking object with WASD
                    case SDLK_w: block.y -= 5; break;
                    case SDLK_s: block.y += 5; break;
                    case SDLK_a: block.x -= 5; break;
                    case SDLK_d: block.x += 5; break;
                }
            }
        }

        // Clear screen
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        // Draw anti-aliased rays in yellow
        for (int i = 0; i < NUM_RAYS; i++) {
            float angle = (2 * M_PI / NUM_RAYS) * i;
            float dx = cosf(angle);
            float dy = sinf(angle);
            float px = lightX;
            float py = lightY;
            bool hit = false;

            for (float t = 0; t < MAX_DIST; t += STEP) {
                px = lightX + dx * t;
                py = lightY + dy * t;
                if (px < 0 || px >= WIDTH || py < 0 || py >= HEIGHT) break;
                if (px >= block.x && px <= block.x + block.w && py >= block.y && py <= block.y + block.h) {
                    aalineRGBA(renderer,
                               (Sint16)lightX, (Sint16)lightY,
                               (Sint16)px, (Sint16)py,
                               255, 255, 0, 255);
                    hit = true;
                    break;
                }
            }
            if (!hit) {
                float endX = lightX + dx * MAX_DIST;
                float endY = lightY + dy * MAX_DIST;
                aalineRGBA(renderer,
                           (Sint16)lightX, (Sint16)lightY,
                           (Sint16)endX, (Sint16)endY,
                           255, 255, 0, 255);
            }
        }

        // Draw blocking object in red
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRect(renderer, &block);

        // Draw light source as a small white square
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_Rect lightRect = {(int)lightX - 5, (int)lightY - 5, 10, 10};
        SDL_RenderFillRect(renderer, &lightRect);

        SDL_RenderPresent(renderer);
        SDL_Delay(16); // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

/*
 * Compile with:
 *   gcc ray_tracer.c -o ray_tracer -lSDL2 -lSDL2_gfx -lm
 * Controls:
 *   Arrow keys to move light source
 *   WASD to move the blocking object
 *   ESC to quit
 */
