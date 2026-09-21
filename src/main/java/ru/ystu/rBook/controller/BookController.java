package ru.ystu.rBook.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import ru.ystu.rBook.domain.Book;
import ru.ystu.rBook.service.BookService;

import java.io.FileNotFoundException;

@Controller
@RequiredArgsConstructor
public class BookController {
    private final BookService service;

    @ResponseStatus(value = HttpStatus.NOT_FOUND, reason = "Not Found")
    @ExceptionHandler(FileNotFoundException.class)
    public void fileNotFoundHandler() {

    }

    @GetMapping("/list")
    public String getAll(Model model) {
        model.addAttribute("list", service.getAll());
        return "list";
    }

    @PostMapping(value = "/book", consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
    public String newBook(Book book, Model model) {
        service.create(book);
        return getAll(model);
    }

    @GetMapping("/book/{id}")
    public String getBook(@PathVariable Long id, Model model) throws FileNotFoundException {
        model.addAttribute("book", service.get(id));
        return "book";
    }

    @GetMapping("/book/rm/{id}")
    public String rmBook(@PathVariable Long id, Model model) {
        service.delete(id);
        return "redirect:/list";
    }
}
