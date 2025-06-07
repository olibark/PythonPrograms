#include <gtk/gtk.h>
#include <stdlib.h>
#include <time.h>

static int target;
static int attempts = 0;
static GtkWidget *entry;
static GtkWidget *label;

static void on_guess_clicked(GtkButton *button, gpointer user_data) {
    const char *text = gtk_entry_get_text(GTK_ENTRY(entry));
    int guess = atoi(text);
    attempts++;
    char buf[128];
    if (guess < target) {
        snprintf(buf, sizeof(buf), "Too low!");
    } else if (guess > target) {
        snprintf(buf, sizeof(buf), "Too high!");
    } else {
        snprintf(buf, sizeof(buf), "Correct! You guessed in %d attempts.", attempts);
        gtk_widget_set_sensitive(GTK_WIDGET(button), FALSE);
    }
    gtk_label_set_text(GTK_LABEL(label), buf);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);
    srand((unsigned)time(NULL));
    target = rand() % 100 + 1;

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Guessing Game");
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(window), vbox);

    label = gtk_label_new("Guess a number between 1 and 100");
    gtk_box_pack_start(GTK_BOX(vbox), label, FALSE, FALSE, 0);

    entry = gtk_entry_new();
    gtk_box_pack_start(GTK_BOX(vbox), entry, FALSE, FALSE, 0);

    GtkWidget *button = gtk_button_new_with_label("Guess");
    g_signal_connect(button, "clicked", G_CALLBACK(on_guess_clicked), NULL);
    gtk_box_pack_start(GTK_BOX(vbox), button, FALSE, FALSE, 0);

    gtk_widget_show_all(window);
    gtk_main();
    return 0;
}
