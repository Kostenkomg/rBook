package ru.ystu.rBook.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import ru.ystu.rBook.domain.Book;
import ru.ystu.rBook.service.BookService;

import javax.annotation.PostConstruct;

@Configuration
@RequiredArgsConstructor
public class BookConfig {
    private final BookService service;

    @PostConstruct
    public void init() {
        service.create(new Book(1L, "Война и Мир", "1867", "Л.Н.Толстой", "роман"));
        service.create(new Book(2L, "На Дне", "1902", "М.Горький", "пьеса"));
        service.create(new Book(3L, "Идиот", "1868", "Ф.М.Достоевский", "роман"));
        service.create(new Book(4L, "Бесприданница", "1878", "А.Н.Островский", "пьеса"));
        service.create(new Book(5L, "Вольность", "1938", "А.Н.Радищев", "ода"));
    }
}
